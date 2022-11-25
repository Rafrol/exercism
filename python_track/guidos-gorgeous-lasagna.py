#Time the lasagna should be in the oven according to the cookbook.
EXPECTED_BAKE_TIME = 40
#Preparation time of each layer according to the cookbook
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time of the lasagna.
 
    :param number_of_layers: int the number of lasagna layers
    :return: int amount of prep time (in minutes), considering on 2 minutes per layer
    """
    return number_of_layers * PREPARATION_TIME
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the lasagna's bake time remaining up to the end.
 
    :param elapsed_bake_time: int the time that the lasagna is already being baked
    :return: int the remaining baking time up to the lasagna be done
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the lasagna's total time to be prepaired considering the total preparation time plus the baking time.
 
    :param elapsed_bake_time: int the time that the lasagna is already being baked
    :param preparation_time_in_minutes(number_of_layers) int the total preparation time considering the number of layers
    :return: int the total preparation time plus the all the baking time
    """
    return preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time
