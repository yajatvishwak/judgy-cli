import os,json
import click

def write(output_location,title ,output, file_suffix):
    if not os.path.exists(output_location):
        os.makedirs(output_location)
    if output_location:
        if os.path.isdir(output_location):
            with open(
                os.path.join(output_location, title + file_suffix), "w"
            ) as outfile:
                json.dump(output, outfile)
        else:
            with open(output_location, "w") as outfile:
                json.dump(output, outfile)
    else:
        click.echo(json.dumps(output))