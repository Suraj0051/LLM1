__copyright__ = 'Copyright (C) Infineon Technologies (2024)'

from pathlib import Path
from setuptools import find_packages, setup

from ai_toolbox.ai_toolbox_version.version import VERSION

NAME = 'ai-toolbox'
DESCRIPTION = 'The AI Toolbox composes various tools built using the various AI Models'
REQUIRES_PYTHON = '>=3.12.1'
REQUIRED = [
    # required Python packages (dependencies)
    'aiohttp==3.9.1',
    'aiosignal==1.3.1',
    'attrs==23.2.0',
    'certifi==2023.11.17',
    'charset-normalizer==3.3.2',
    'click==8.1.7',
    'colorama==0.4.6',
    'docopt==0.6.2',
    'frozenlist==1.4.1',
    'idna==3.6',
    'markdown-it-py==3.0.0',
    'mdurl==0.1.2',
    'multidict==6.0.4',
    'openai==0.28.0',
    'pipreqs==0.4.13',
    'Pygments==2.17.2',
    'requests==2.31.0',
    'rich==13.7.0',
    'setuptools==69.0.3',
    'tqdm==4.66.1',
    'urllib3==2.1.0',
    'wget==3.2',
    'wheel==0.42.0',
    'yarg==0.1.9',
    'yarl==1.9.4',
]

here = Path(__file__).parent

# Import the README and use it as the long-description.
with here.joinpath('Readme.md').open(encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Import the LICENSE and use it as the package license.
with here.joinpath('LICENSE.txt').open(encoding='utf-8') as f:
    _license = '\n' + f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ajith Padman(IFAG ATV MC PAI SW SAI)',
    author_email='ajith.padman@infineon.com',
    url='https://bitbucket.vih.infineon.com/projects/ATVSWMEG/repos/mc_sw_meg_ai/browse',
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests', 'docs', 'utilities')),
    entry_points={},
    install_requires=REQUIRED,
    include_package_data=True,
    license=_license,
    classifiers=[
        # Full list: https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',

    ]
)
