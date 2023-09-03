single_cookie_grams = 25
cup = 140
small_spoon = 10
big_spoon = 20
cookies_per_box = 5

batches = int(input())

ingredients = []

flour = 0
sugar = 0
cocoa = 0
ttl_boxes = 0
for idx in range(batches):
    flour = int(input())
    sugar = int(input())
    cocoa = int(input())
    ingredients.append((flour, sugar, cocoa))

    flour_cups = int(flour / cup)
    sugar_spoon = int(sugar / big_spoon)
    cocoa_spoon = int(cocoa / small_spoon)
    ttl_cookies_per_bake = ((cup + small_spoon + big_spoon) *
                            min(flour_cups, sugar_spoon, cocoa_spoon)) / single_cookie_grams
    boxes_per_patch = int(ttl_cookies_per_bake / cookies_per_box)
    if boxes_per_patch > 0:
        print(f"Boxes of cookies: {boxes_per_patch}")
    else:
        print("Ingredients are not enough for a box of cookies.")
    ttl_boxes += boxes_per_patch

print(f"Total boxes: {ttl_boxes}")
