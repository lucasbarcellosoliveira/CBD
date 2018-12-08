# from Record import *
import os


class Block:
    def __init__(self, disk_name):
        """ Constructor """
        # open disk file
        if (os.path.isfile('./' + disk_name)):
            self.disk = open(disk_name, "r+")
        else:
            self.disk = open(disk_name, "w+")
        # set size of block
        self.max_size = 8
        # set number of operations (read/write)
        self.n_op = 0
        # set list of records
        self.records = []
        # record size
        self.record_size = 138
        self.pos = 0

    def __del__(self):
        """ Destructor """
        # persist last records to disk
        self.persist(self.disk.tell())
        # close disk file
        self.disk.close()

    def persist(self, pos):
        """ Persists current block's records to the disk file """
        # add 1 to number of operations
        self.n_op += 1
        # position the pointer at the writing location
        self.disk.seek(pos)
        # persist each block record to disk file
        for rec in self.records:
            self.disk.write(str(rec))
        self.disk.flush()
        # reset list of records
        self.records = []

    def write(self, pos, rec):
        """ Write record rec in position pos of the disk file """
        if (len(self.records) >= self.max_size):
            self.persist(pos)
        self.records += [rec]
        self.pos = pos

    def read(self, pos):
        """ Add records of pos position in disk file to this """
        self.n_op += 1
        self.records = []
        self.disk.seek(pos)
        while (len(self.records) < self.max_size):
            self.records += [self.disk.read(self.record_size)]


# r = Record("11111111111;54.037.661-5;estermoro@gmail.com;06/01/1952;Feminino;Yuri Matheus Antonia;5942.00")
# b = Block("out.txt")
# b.write(500, str(r))
# b.persist(500)
# b.read(0)
