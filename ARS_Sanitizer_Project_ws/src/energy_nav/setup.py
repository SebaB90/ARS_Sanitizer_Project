from setuptools import find_packages, setup

package_name = 'energy_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sebab',
    maintainer_email='sebastiano.bertame@studio.unibo.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'energy_nav_node = energy_nav.energy_navigation:main',
            'example_nav_node = energy_nav.example_navigation:main',
        ],
    },
)
