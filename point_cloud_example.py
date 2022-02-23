import pyzed.sl as sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.ULTRA # Use ULTRA depth mode
init_params.coordinate_units = sl.UNIT.MILLIMETER # Use millimeter units (for depth measurements)

# Opens the ZED camera from the provided InitParameters and exits if it fails.
err = zed.open(init_params)
if (err != sl.ERROR_CODE.SUCCESS) :
    exit(-1)

if zed.grab() ==  sl.ERROR_CODE.SUCCESS :
    # Create a matrix
    point_cloud = sl.Mat()
    #using sl.MEASURE because this it for data collection, XYZBGRA = saves coordinates aswell as colors
    #Color is a 32bit value which consists of 4 8bit values concatinated. 
    # Each of these values represents Blue, Green, Red and Alpha respectivly.
    zed.retrieve_measure(point_cloud, sl.MEASURE.XYZBGRA)


    print(point_cloud)
    #prints: n/a Ts 1645543508642010100 sl::Mat of size [1280,720], with 4 channels of type float allocated on CPU (memory owned).

    #get_data() converts a sl.Mat to a numpy matrix
    nparr = point_cloud.get_data()

    print(nparr)
    #prints: your typical numpy 1280x720x4 matrix where the values are x,y,z and color

zed.close()