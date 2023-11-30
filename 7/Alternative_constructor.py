class PC():
    pc_counter=0
    def __init__(self,cpu,gpu,ram_slot1,ram_slot2):
        self.cpu=cpu
        self.gpu=gpu
        self.ram_slot1=ram_slot1
        self.ram_slot2=ram_slot2
        self.overall_ram=self.ram_slot2+self.ram_slot1
        PC.pc_counter+=1
        
    def Show_info(self):
        print(f"CPU: {self.cpu}\nGPU: {self.gpu}\nram slot 1: {self.ram_slot1}\nram slot 2: {self.ram_slot2}\noverall ram: {self.overall_ram}")
    @classmethod
    def Alt_constructor(cls,cpu,gpu,ram_slot1,ram_slot2):
        ram_slot1_x2=ram_slot1*2
        ram_slot2_x2=ram_slot2*2
        return PC(cpu,gpu,ram_slot1_x2,ram_slot2_x2)
    
ob1=PC("Ryzen 5","GTX 1060",8,8)
ob2=PC.Alt_constructor("Ryzen 5","GTX 1060",8,8)
ob1.Show_info()
ob2.Show_info()