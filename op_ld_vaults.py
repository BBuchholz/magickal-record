# TODO: mimic SelectCartFileMenu
# list all .md files in the config folder 
# and allow user to select which to load 
# from, this will give us the option of 
# loading multiple configurations and 
# creating granular archives that can hold 
# specific subdomains of larger vaults 
# without having to load soooooo many 
# files every time


# NB: Should Be able to reuse SelectFileOp
# for the files to list

# Mostly just need to replace 
# self.cart.get_cart_files() 
# with self.obio.get_config_files()