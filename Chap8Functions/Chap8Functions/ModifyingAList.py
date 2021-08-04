##Chapter 8 Exercise 9-11
NeededItems = ['swimsuit', 'sandals', 'sunscreen', 'beach towel']
CompletedPacking = []
InSuitcase = ""
Packed = ""

def PackingList (NeededItems, CompletedPacking):
    """Printed each item in list until none are left. Moved each item to new list once displayed."""
    while NeededItems:
        InSuitcase = NeededItems.pop()
        print (f"Packing: {InSuitcase}")
        CompletedPacking.append(InSuitcase)

def ShowingPackedItems (CompletedPacking):
    """Shows all of the items that have been packed."""
    for Packed in CompletedPacking:
        print (f"\n{Packed.title()} has been packed.")

PackingList(NeededItems, CompletedPacking)
ShowingPackedItems (CompletedPacking)