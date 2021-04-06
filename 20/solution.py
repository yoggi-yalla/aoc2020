with open('input.txt', 'r') as f:
    data = f.read()
    tiles_ = data.split('\n\n')

class PixelObj:
    identifier = None
    orientation = 0

    def next_orientation(self):
        if self.orientation in [7,3]:
            self.flip_vertical()
        else:
            self.rotate_cw()
        self.orientation = (self.orientation + 1) % 8 

    def transpose(self):
        self.pixels = list(map(list,zip(*self.pixels)))
        
    def flip_vertical(self):
        self.pixels = list(reversed(self.pixels))

    def rotate_cw(self):
        self.flip_vertical()
        self.transpose()
    
    def show(self):
        if self.identifier:
            print(f"\n{self.identifier}:")
        else:
            print(f"\nImage:")
        for row in self.pixels:
            print("".join(row))

class Image(PixelObj):
    def __init__(self, dim):
        self.dim = dim
        self.pixels = [["." for _ in range(dim*8)] for _ in range(dim*8)]
        self.tiles = [[None for _ in range(dim)] for _ in range(dim)]

    def count_roughness(self):
        count = 0
        for i in range(self.dim*8):
            for j in range(self.dim*8):
                if self.pixels[i][j] == "#":
                    count += 1
        return count

    def paint_dragons(self, fingerprint, width, height):
        for i in range(self.dim*8 - height):
            for j in range(self.dim*8 - width):
                if all(self.pixels[i+x][j+y] == "#" for x,y in fingerprint):
                    for x,y in fingerprint:
                        self.pixels[i+x][j+y] = "O"

    def update(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.tiles[i][j]:
                    for t_i in range(1,9):
                        for t_j in range(1,9):
                                self.pixels[t_i + i*8 - 1][t_j + j*8 - 1] = self.tiles[i][j].pixels[t_i][t_j]


class Tile(PixelObj):
    def __init__(self, tile):
        rows = tile.split('\n')[1:]

        self.identifier = int(tile[5:9])
        self.pixels = [[ch for ch in row] for row in rows]

    def top_edge(self):
        return "".join(self.pixels[0])

    def bottom_edge(self):
        return "".join(self.pixels[9])
    
    def left_edge(self):
        return "".join(r[0] for r in self.pixels)
    
    def right_edge(self):
        return "".join(r[9] for r in self.pixels)

    def hashes(self):
        hashes = []
        for e in [self.top_edge(), self.bottom_edge(), self.left_edge(), self.right_edge()]:
            rev = e[::-1]
            hashes.append(e if e > rev else rev)
        return hashes

    def is_valid_top_left_corner(self, others):
        top_hash = self.hashes()[0]
        left_hash = self.hashes()[2]
        for t in others:
            if t == self:
                continue
            elif any(top_hash == h for h in t.hashes()):
                return False
            elif any(left_hash == h for h in t.hashes()):
                return False
        return True

    def pairs_with(self, other):
        if self == other:
            return False
        for h in self.hashes():
            if any(h == h_ for h_ in other.hashes()):
                return True
        return False
    
    def matching_top(self, other):
        return self.top_edge() == other.bottom_edge()
    
    def matching_left(self, other):
        return self.left_edge() == other.right_edge()


tiles = [Tile(t) for t in tiles_]

corner_tiles = []
for t in tiles:
    count = 0
    for other in tiles:
        if t.pairs_with(other):
            count += 1
    if count == 2:
        corner_tiles.append(t)


part_1 = 1
for t in corner_tiles:
    part_1 *= t.identifier
print("Part 1:", part_1)



# Part 2:
dim = 12
img = Image(dim)

# Place top left corner
top_left = corner_tiles[0]
for _ in range(8):
    if top_left.is_valid_top_left_corner(tiles):
        break
    top_left.next_orientation()
img.tiles[0][0] = top_left

# Place top row
for j in range(1,dim):
    for t in tiles:
        for _ in range(8):
            if t.matching_left(img.tiles[0][j-1]):
                img.tiles[0][j] = t
                break
            t.next_orientation()
        if img.tiles[0][j]:
            break

# Place remaining rows
for i in range(1,dim):
    for j in range(dim):
        for t in tiles:
            for _ in range(8):
                if t.matching_top(img.tiles[i-1][j]):
                    img.tiles[i][j] = t
                    break
                t.next_orientation()
            if img.tiles[i][j]:
                break

# Transfer tiles to img pixels
img.update()

dragon = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

dragon_pixels = [[ch for ch in row] for row in dragon.split('\n')]
dragon_fingerprint = []
for i in range(3):
    for j in range(20):
        if dragon_pixels[i][j] == '#':
            dragon_fingerprint.append((i,j))

for _ in range(8):
    img.paint_dragons(dragon_fingerprint, 20, 3)
    img.next_orientation()

print("Part 2:",img.count_roughness()) # 2065 


# Finished image:
"""
[img.next_orientation() for _ in range(4)]
img.show()
"""
