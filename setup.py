from distutils.core import setup

setup(
  name = 'github_action_test',
  packages = ['github_action_test'],
  version = '0.1.0',
  license='MIT',
  description = 'GitHub Action workflow test',
  author = 'KOUA ELYSEE',
  author_email = 'elyseekevin49@gmail.com',
  url = 'https://github.com/elysee-01/github_action_test',
  download_url = 'https://github.com/elysee-01/github_action_test/archive/refs/tags/0.1.0.tar.gz',
  keywords = ['python', 'github'],
  package_data={},
  include_package_data=True,
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
