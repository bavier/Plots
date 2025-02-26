import setuptools

package = 'Plots'
version = '0.6.2'

setuptools.setup(
    name=package,
    version=version,
    description="A graph plotting app for GNOME",
    packages=setuptools.find_packages(exclude=['tests']),
    package_data={
        "plots.ui": ["*.glade"],
        "plots": ["shaders/*.glsl"],
        "plots.res": ["*.svg", "*.ttf"],
        "plots.locale": ["*/LC_MESSAGES/*.mo"],
    },
    install_requires=[
        "PyGObject",
        "PyOpenGL",
        "Jinja2",
        "numpy",
        "lark",
        "PyGLM",
        "freetype-py",
    ],
    python_requires='~=3.6',
    entry_points={
        "gui_scripts": [
            "plots=plots:main"
        ],
    },
)
