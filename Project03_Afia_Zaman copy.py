# AFIA ZAMAN
# Constants6
WIDTH_AND_HEIGHT = 12 * 24
COST_OF_EACH_WOOD = 24.99
BORDER_HEIGHT = 6
SIDES_PER_HEXAGON = 6

# User input
side_length = int(input("Enter the side length of hexagon = "))
num_of_hexagons = int(input("Enter the number of hexagons = "))

# Calculate hexagon area
hexagon_area = (3 * (3 ** (1/2))/2) * (side_length ** 2)

# Calculate total wood area
total_wood_area = num_of_hexagons * hexagon_area

# Needed sheets for the main hexagons
needed_sheets = total_wood_area / WIDTH_AND_HEIGHT

# Wood cost for the main hexagons
wood_cost = needed_sheets * COST_OF_EACH_WOOD

#Extension
# Calculate border area and cost
border_area_per_hexagon = BORDER_HEIGHT * SIDES_PER_HEXAGON
total_border_area = border_area_per_hexagon * num_of_hexagons
border_sheets_needed = total_border_area / WIDTH_AND_HEIGHT
border_cost = border_sheets_needed * COST_OF_EACH_WOOD

# Print
print("Total wood area = {:.3f}".format(total_wood_area))
print("Sheets of wood needed = {:.3f}".format(needed_sheets))
print("wood cost = ${:.2f}".format(wood_cost))
print("border cost = ${:.2f}".format(border_cost))



# Followup answers :

"""
1. I did the project part by part, so I completed it in a long time!
2. Yes.
3. Finding formulas
4. Different mathematical problem
5. I searched for formula in google

"""










