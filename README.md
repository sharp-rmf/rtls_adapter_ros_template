# rtls_adapter_ros_template

Inspired by the open-rmf adapter templates on open-rmf, this package aims to provide developers with a baseline python-based RTLS adapter to integrate into the ROS eco-system.


## Step 1: Fill in the blanks
Fill up the section of the codes which make the respective API calls to the RTLS system/device. These section will be indicated as `IMPLEMENT YOUR CODE HERE`.

Most of the additional inputs will be found in the `RTLSClientAPI.py` file which defines some of the core functionality the RTLS requires and the communication menas with the devices involved. For example, if your device connects and provides location information via Serial, then the `rtlsAPI::get_position()` function may be implemented as below
```
def get_pos(self):
    try:
        data = self.ser.read(9999)
        x_index  = int(data.find(self.x_key.encode()))
        x = data[(x_index + self.key_len):(x_index + self.key_len + 4)]
        y_index  = int(data.find(self.y_key.encode()))
        y = data[(y_index + self.key_len):(y_index + self.key_len + 4)]
        return (x, y, 0)
    except Exception as err:
        print(f"Error: {err}")
    return None
```


## Step 2: Update reference coordinates on config.yaml
The `config.yaml` file contains important reference coordinate information which comprises of two sets of [x,y] coordinates that corresponds of the same points but based on the RTLS device's specific coordinate frame and the RMF global coordinate frame. For an accurate estimated coordinate transformation, a minimum of 4 matching points will be needed.


## Step 3: Adapter Execution
Run the command below while passing the paths to the configuration file that the rtls operates on.
```
ros2 run rtls_adapter_ros_template rtls_adapter -c ~/<workspace>/src/rtls_adapter_ros_template/config/config.yaml
```


## Step 4: Customise package [Optional]
Since this is a template package, you can choose to make name changes to the various files in the package to make it unique. The following files will need some minor renaming:

1) `setup.py`: change to be done to package name & entry point input
2) `setup.cfg`: rename the package base libraries accordingly (i.e. rtls_adapter_ros_template change to rtls_adapter_XXX)
3) `package.xml`: rename package name
4) `rtls_adapter_ros_template` folder: rename to new package name
5) `RTLSAdapter.py`: `<new_folder_name>.RTLSClientAPI import rtlsAPI`
