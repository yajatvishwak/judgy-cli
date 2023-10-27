# # keep for chroma ----
# __import__("pysqlite3")
# import sys

# sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
# # ----

from git import Repo
import os
import shutil

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser

from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.output_parsers import PydanticOutputParser
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


from llm import LLMModels
from .output_parsers import FeaturesImplementation, ClaimedFeatureList
from .prompts import claimed_features_prompt, code_implementation_prompt

FOLDERS_TO_REMOVE = [
    "node_modules",
    "dist",
    "env",
    "build",
    "static",
    "public",
    "assets",
    "tests",
    "test",
    "docs",
    "media",
    "gradle",
    "node_modules",
    "static",
]
SUFFIXES_TO_LOAD = [
    ".py",
    ".js",
    ".jsx",
    ".tsx",
    ".ts",
    ".php",
    ".go",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".r",
    ".kt",
    ".rb",
]


class CodeAgent:
    def __init__(self, summary, title, git_link, repo_download_location="") -> None:
        self.summary = summary
        self.llm = LLMModels.get_openai_model()
        self.chat_llm = LLMModels.get_openai_model()
        self.repo_download_location = repo_download_location
        self.project_name = title
        self.git_link = git_link
        self.git_location = os.path.join(
            self.repo_download_location, self.project_name
        )  # location where the code will be cloned locally

    def score(self):
        features = self.find_claimed_features()
        self.preprocess_git(features=features)
        loader = GenericLoader.from_filesystem(
            self.git_location,
            glob="**/*",
            suffixes=SUFFIXES_TO_LOAD,
            parser=LanguageParser(parser_threshold=700),
        )
        splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        documents = loader.load()
        texts = splitter.split_documents(documents)

        if len(texts) == 0:
            return self.empty_implementation(features=features)
        db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
        parser = PydanticOutputParser(pydantic_object=FeaturesImplementation)
        retriever = db.as_retriever(
            search_type="mmr",  # Also test "similarity"
            search_kwargs={"k": 10},
        )
        implementation = []
        for feature in features:
            memory = ConversationSummaryMemory(
                llm=self.chat_llm,
                memory_key="chat_history",
                return_messages=True,
            )
            question = """{}""".format(feature.featureName)
            qa = ConversationalRetrievalChain.from_llm(
                self.chat_llm,
                retriever=retriever,
                memory=memory,
                verbose=False,
                max_tokens_limit=4000,
            )

            result = qa(question)["answer"]
            prompt = PromptTemplate(
                template=code_implementation_prompt,
                input_variables=["feature_name", "feature_description", "question"],
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                },
            )
            try:
                output = self.llm(
                    prompt.format_prompt(
                        feature_name=feature.featureName,
                        feature_description=result,
                        question=question,
                    ).to_string()
                )
                try:
                    f = parser.parse(output)
                except:
                    fixing_parser = OutputFixingParser.from_llm(
                        parser=parser, llm=self.chat_llm
                    )
                    f = fixing_parser.parse(output)

            except Exception as e:
                raise e
                f = FeaturesImplementation(
                    featureName=feature.featureName,
                    implementationStatus="Detection Failed",
                    explanation="Was not able to process this rightly",
                )
            implementation.append(f)
        db.delete_collection()
        return implementation

    def empty_implementation(self, features):
        fin = []
        for claimed_code in features:
            f = FeaturesImplementation(
                featureName=claimed_code.featureName,
                explanation="No gitlink provided",
                featureDescription="",
                implementationStatus="Not Implemented",
            )
            fin.append(f)
        return fin

    def remove_folders(self, directory):
        for dirpath, dirname, _ in os.walk(directory, topdown=False):
            for folder_name in FOLDERS_TO_REMOVE:
                if folder_name in dirname:
                    folder_path = os.path.join(dirpath, folder_name)
                    shutil.rmtree(folder_path)

    def preprocess_git(self, features):
        # 1. download repo from github
        if os.path.isdir(self.git_location):
            pass
        else:
            try:
                Repo.clone_from(self.git_link, to_path=self.git_location)
            except Exception as e:
                return self.empty_implementation(features)
        # 2. remove build folders
        self.remove_folders(directory=self.git_location)

    def find_claimed_features(self):
        # 3. find claimed features
        try:
            parser = PydanticOutputParser(pydantic_object=ClaimedFeatureList)
            prompt = PromptTemplate(
                template=claimed_features_prompt,
                input_variables=["ideasummary"],
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                },
            )

            output = self.llm(
                prompt.format_prompt(ideasummary=self.summary).to_string()
            )
            try:
                claimed_features = parser.parse(output)
            except:
                fixing_parser = OutputFixingParser.from_llm(
                    parser=parser, llm=self.chat_llm
                )
                claimed_features = fixing_parser.parse(output)
            return claimed_features.featureList
        except Exception as e:
            raise e
