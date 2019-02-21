from setuptools import find_packages, setup

packages = find_packages(
    where='./',
    include=['octicons', 'octicons.*'],
)
if not packages:
    raise ValueError('No packages detected.')


with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='octicons',
    version='1.4.2',
    description='A Python port of GitHub\'s Octicons, with Django support',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.4',
    url='https://github.com/leesdolphin/octicons',
    author='Opal Symes',
    author_email='python@opal.codes',
    license='LGPLv3+',
    packages=packages,
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
