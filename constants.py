import arcade

# Map
PADDING = 25
NB_TILES = 15
TILE_SIZE = 50
OBJ_SIZE = TILE_SIZE - 10
MAP_SIZE = NB_TILES * TILE_SIZE
NB_OBJ = 20
PETIT_SIZE = OBJ_SIZE*0.3
MOYEN_SIZE = OBJ_SIZE*0.6
GRAND_SIZE = OBJ_SIZE
NB_WATER_TILES = 4

# Buttons
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 150

# Right menu
MENU_X = MAP_SIZE + 2*PADDING
MENU_WIDTH = BUTTON_WIDTH * 2 + PADDING

# Screen
SCREEN_WIDTH = MAP_SIZE + 3*PADDING + MENU_WIDTH
SCREEN_HEIGHT = MAP_SIZE + 2*PADDING

# Point box
POINT_PADDING = 50
POINT_BOX_X = MENU_X + POINT_PADDING
POINT_BOX_Y = SCREEN_HEIGHT - PADDING - POINT_PADDING
POINT_BOX_HEIGHT = 60
LOGO_SIZE = 50

# Inventory
INVENTORY_SIZE = 3
INVENTORY_TITLE_Y = POINT_BOX_Y - POINT_BOX_HEIGHT - PADDING
INVENTORY_TITLE_HEIGHT = 25
INVENTORY_TEXT_HEIGHT = 30
INVENTORY_BOX_PADDING = 10
INVENTORY_BOX_Y = INVENTORY_TITLE_Y - INVENTORY_TITLE_HEIGHT
INVENTORY_BOX_HEIGHT = INVENTORY_TEXT_HEIGHT*INVENTORY_SIZE + INVENTORY_BOX_PADDING
INVENTORY_TEXT_X = MENU_X + INVENTORY_BOX_PADDING
INVENTORY_TEXT_Y = INVENTORY_BOX_Y - INVENTORY_TEXT_HEIGHT
INVENTORY_BUTTON_Y = INVENTORY_BOX_Y - INVENTORY_BOX_HEIGHT - PADDING
INVENTORY_BUTTON_HEIGHT = BUTTON_HEIGHT

# Instructions
INSTRUCTION_TITLE_Y = INVENTORY_BUTTON_Y - INVENTORY_BUTTON_HEIGHT - 2*PADDING
INSTRUCTION_TITLE_HEIGHT = 25
INSTRUCTION_BOX_PADDING = 10
INSTRUCTION_BOX_Y = INSTRUCTION_TITLE_Y - INSTRUCTION_TITLE_HEIGHT
INSTRUCTION_BOX_HEIGHT = 2*INSTRUCTION_BOX_PADDING + 150
INSTRUCTION_TEXT_X = MENU_X + INSTRUCTION_BOX_PADDING
INSTRUCTION_TEXT_Y = INSTRUCTION_BOX_Y - INSTRUCTION_BOX_PADDING
INSTRUCTION_TEXT_HEIGHT = INSTRUCTION_BOX_HEIGHT - 2*INSTRUCTION_BOX_PADDING
INSTRUCTION_TEXT_WIDTH = MENU_WIDTH - 2*INSTRUCTION_BOX_PADDING
INSTRUCTION_BUTTON_Y = INSTRUCTION_BOX_Y - INSTRUCTION_BOX_HEIGHT - PADDING
INSTRUCTION_BUTTON_HEIGHT = BUTTON_HEIGHT

# Other
MOVE_DELAY = 0.2  # 250 ms
BACKGROUND_COLOR = (250, 235, 235)
BUTTON_MAUVE = {'bg_color': arcade.color.MAUVE_TAUPE}
BUTTON_TUSCANY = {'bg_color': arcade.color.TUSCANY}
