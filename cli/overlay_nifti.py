import os
import click
import mpld3
import tempfile
import webbrowser
import matplotlib as mpl
from nilearn import plotting
import matplotlib.pyplot as plt

def write_html(html, title):
    
    body = f"""
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
        <b>
        <p>{title}</p>
        </b>
        {html}
        <br>
        <br>
    """
    return body

def setup_browser(body, nobrowser, save):

    html_template = f"""
    <html>
    <head></head>
    <body>
        {body}
    </body>
    </html>
    """
    
    if nobrowser or save:
        file = open(save, "w")
        file .write(html_template)
        file.close
    elif not nobrowser and not save:
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_file:
            temp_file.write(html_template.encode('utf-8'))
            filename = 'file:///'+ temp_file.name
            webbrowser.open_new_tab(filename)
    
    return

def process_option(ctx, param, value):
    if value is not None:
        values = value.split(',')
        return [val.strip() for val in values]

@click.command()
@click.option('--anat','-a', nargs=1, type=str, required=True, 
              help='Path to anatomical nifti image that will ' 
              'be the underlay brain image. This image '
              'is usuallu in MNI152 template space')
@click.option('--overlay','-o', required=True, 
              callback=process_option, help='Path to nifti '
             'image that will overlay the anatimcal image.')
@click.option('--nobrowser', is_flag=True, help='Please add this '
              'flag if you are not on a system that has a web '
              'broweser.')
@click.option('--save', type=str, help='If you would like to save '
              'the html report automatically, supply the name and '
              'path name for the report.')

def overlay_nifti(anat=None, overlay=None, nobrowser=False, save=None):
    if nobrowser and not save:
        raise Exception("""
                        You selected flag `--nobroswer`, but did not 
                        add where to save the html report. Please add 
                        path and file name using `--save` flag. 
                        Example: 
                        `--save /path/to/file.html`
                        """)
    click.echo("\n***** overlaying your images  ＼＿ﾍ(◕‿◕✰)  *******")

    anat_name = (os.path.basename(anat)).replace('.nii.gz', '')
    body_html = ''

    for overlay_img in overlay:
        overlay_name = (os.path.basename(overlay_img)).replace('.nii.gz', '')

        title = f'{anat_name} image\n with overlay\n {overlay_name}'

        fig= plt.figure(figsize=(5,3))
        display = plotting.plot_img(anat,  cmap=mpl.cm.get_cmap('gray'), 
                                     cut_coords=[0,0,0], figure=fig, 
                                     display_mode='ortho', alpha=1, draw_cross=False)
        display.add_overlay(overlay_img, cmap=plotting.cm.red_transparent, alpha=0.5, colorbar=True)
        
        html = mpld3.fig_to_html(fig)
        
        body_html += write_html(html, title)

    setup_browser(body_html, nobrowser, save)


if __name__ == '__main__':
    overlay_nifti()