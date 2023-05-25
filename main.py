import click
from command import overlay_nifti

@click.group(help='CLI to visualize overlays of '
             'various masks over nifti image')

def cli():
    pass

cli.add_command(overlay_nifti.overlay_nifti)

if __name__ == '__main__':
    cli()