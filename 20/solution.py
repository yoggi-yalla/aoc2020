from abc import ABC
import math
import textwrap

class PixelObj(ABC):
    # Sub-classes should have a 'pixels' attribute (list of lists)
    identifier = None
    orientation = 0

    def orientations(self):
        yield self
        for _ in range(7):
            self.next_orientation()
            yield self

    def next_orientation(self):
        if self.orientation in [7,3]:
            self.flip_vertical()
        else:
            self.rotate_cw()
        self.orientation = (self.orientation + 1) % 8 
        
    def flip_vertical(self):
        self.pixels = [row for row in reversed(self.pixels)]

    def rotate_cw(self):
        self.pixels = [[p for p in col[::-1]] for col in zip(*self.pixels)]
    
    def top_edge(self):
        return "".join(self.pixels[0])

    def bottom_edge(self):
        return "".join(self.pixels[-1])
    
    def left_edge(self):
        return "".join(r[0] for r in self.pixels)
    
    def right_edge(self):
        return "".join(r[-1] for r in self.pixels)

    def all_edges(self):
        normal_edges = [self.top_edge(),self.bottom_edge(),self.left_edge(),self.right_edge()]
        reversed_edges = [e[::-1] for e in normal_edges]
        return set(normal_edges + reversed_edges)

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

    @classmethod
    def from_tiles(cls, tiles):
        dim = int(math.sqrt(len(tiles)))
        img = Image(dim)

        used_tiles = set()

        # Place top left corner
        corner_piece = Image.get_corner_piece(tiles)
        corner_piece.align_top_left_orientation(tiles)
        img.tiles[0][0] = corner_piece
        used_tiles.add(corner_piece)
        
        # Place top row
        for j in range(1,dim):
            edge_to_the_left = img.tiles[0][j-1].right_edge()
            for t in tiles:
                if t in used_tiles:
                    continue
                for t in t.orientations():
                    if t.left_edge() == edge_to_the_left:
                        img.tiles[0][j] = t
                        used_tiles.add(t)
                        break
                if img.tiles[0][j]:
                    break
        
        # Place remaining rows
        for i in range(1,dim):
            for j in range(dim):
                edge_above = img.tiles[i-1][j].bottom_edge()
                for t in tiles:
                    if t in used_tiles:
                        continue
                    for t in t.orientations():
                        if t.top_edge() == edge_above:
                            img.tiles[i][j] = t
                            used_tiles.add(t)
                            break
                    if img.tiles[i][j]:
                        break
        img.update()
        return img

    @classmethod
    def get_corner_piece(cls, tiles):
        for t in tiles:
            if sum(t.pairs_with(other) for other in tiles) == 3:
                return t
        raise Exception("No corner piece found")

    def update(self):
        # Move pixels from self.tiles to self.pixels
        for i in range(self.dim):
            for j in range(self.dim):
                if self.tiles[i][j]:
                    for t_i in range(8):
                        for t_j in range(8):
                            self.pixels[t_i + i*8][t_j + j*8] = self.tiles[i][j].pixels[t_i+1][t_j+1]

    def mark_image(self, fingerprint):
        size_i = max(fingerprint, key=lambda x: x[0])[0]
        size_j = max(fingerprint, key=lambda x: x[1])[1]

        for i in range(self.dim*8 - size_i):
            for j in range(self.dim*8 - size_j):
                if all(self.pixels[i+x][j+y] == "#" for x,y in fingerprint):
                    for x,y in fingerprint:
                        self.pixels[i+x][j+y] = "O"

    def count_roughness(self):
        return sum(row.count("#") for row in self.pixels)


class Tile(PixelObj):
    def __init__(self, tile):
        rows = tile.split('\n')[1:]
        self.identifier = int(tile[5:9])
        self.pixels = [[ch for ch in row] for row in rows]

    def align_top_left_orientation(self, others):
        for _ in self.orientations():
            if self.is_valid_top_left_corner(others):
                return self
        raise Exception("Could not align top left corner")

    def is_valid_top_left_corner(self, others):
        for other in others:
            if self == other:
                continue
            elif self.top_edge() in other.all_edges():
                return False
            elif self.left_edge() in other.all_edges():
                return False
        return True

    def pairs_with(self, other):
        return bool(set.intersection(self.all_edges(), other.all_edges()))


class Dragon(PixelObj):
    def __init__(self, picture):
        self.pixels = [[ch for ch in row] for row in picture.split('\n')]
    
    def fingerprint(self):
        fingerprint = []
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                if self.pixels[i][j] == '#':
                    fingerprint.append((i,j))
        return fingerprint

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        tiles_ = data.split('\n\n')

    tiles = [Tile(t) for t in tiles_]
    img = Image.from_tiles(tiles)

    # Corners
    c1 = img.tiles[0][0].identifier
    c2 = img.tiles[0][-1].identifier
    c3 = img.tiles[-1][0].identifier
    c4 = img.tiles[-1][-1].identifier

    dragon = Dragon(textwrap.dedent("""\
                                          # 
                        #    ##    ##    ###
                         #  #  #  #  #  #   """))

    for d in dragon.orientations():
        img.mark_image(d.fingerprint())
    
    print("Part 1:", c1*c2*c3*c4) # 51214443014783
    print("Part 2:", img.count_roughness()) # 2065 

    # Finished image:
    '''
    [img.next_orientation() for _ in range(4)]
    img.show()
    '''

main()
