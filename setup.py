from setuptools import setup

package_name = 'rtls_adapter_ros_template'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['config/config.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alphonsus',
    maintainer_email='alphonsustay@github.com',
    description='RTLS Adapter Template',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rtls_adapter = rtls_adapter_ros_template.rtls_adapter:main'
        ],
    },
)
