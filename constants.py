### NB: we are currently moving constants into 
# config files to allow for alternate setups that 
# live side by side, this file will be split into 
# two sections, constants that have migrated and 
# those awaiting migration, move them accordingly 
# as they are tested and transformed


##############################################
###### CONSTANTS THAT HAVE MIGRATED ##########
##############################################

# keep a small subset for testing here
OBSIDIAN_TEST_FOLDER = "~/obsidianTestFolder"
# for testing adjacent vaults
OBSIDIAN_TEST_VAULT_ONE = "~/obsidianTestFolder/testVaultOne"
OBSIDIAN_TEST_VAULT_TWO = "~/obsidianTestFolder/testVaultTwo"
# store external folder addresses in md files 
# in this folder, so they stay out of github
CONFIG_FOLDER = "~/obsidianConfig"
# To Test NONEXISTANT FILES
NONEXISTANT_FILE = "THISFILEDOESNOTEXIST.md"
# To Test Existing files
EXISTANT_FILE = "BasicFile.md"

##############################################
###### CONSTANTS AWAITING MIGRATION ##########
##############################################

# BasicFile with full path
BASIC_MYR_FILE_TEST_PATH = "~/nwd/test/BasicMyrFile.md"
# Folder that doesn't exist
NONEXISTANT_FOLDER = "~/doesNotExist"
# Test Folder
TEST_FOLDER = "~/nwd/test"
# DSV Test Folder
DSV_TEST_FOLDER = "~/nwd/test-dsv"
# Cartographer Folder
CARTOGRAPHER_FOLDER = "~/nwd/cartographer"
# Cets File
CETS_FILE = "~/nwd/cartographer/Cets.md"
# Cartographer test file without any cards
CART_TEST_FILE_NO_CARDS = "TEST_DONOTMODIFY_NoCards.xlsx"
# Cartographer test file with some cards
CART_TEST_FILE_SOME_CARDS = "TEST_DONOTMODIFY_SomeCards.xlsx"