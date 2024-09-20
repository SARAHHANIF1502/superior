class TempController:
    def __init__(self, room_name, target_temp):
        self.room_name = room_name  
        self.target_temp = target_temp  
        self.current_temp = None 
    def update_temp(self, new_temp):
           self.curr_temp = new_temp 
    def control_heater(self): 
         if self.curr_temp > self.target_temp:
            return f"Turn off {self.room_name}'s heater"
         else:
            return f"Turn on {self.room_name}'s heater"
    
room_controllers = {
    "LivingRoom": TempController("LivingRoom", 22),
    "Bedroom": TempController("Bedroom", 20),
    "Office": TempController("Office", 24)
    
}
curr_temp = {
    "LivingRoom": 28,
    "Bedroom": 18,
    "Office": 32
}
for room, controller in room_controllers.items():
    controller.update_temp(curr_temp[room])
    print(f"{room}: {curr_temp[room]}°C ==> {controller.control_heater()}")
new_temp = {
    "LivingRoom": 25,
    "Bedroom": 19,
    "Office": 30
}
for room, controller in room_controllers.items():
    controller.update_temp(new_temp[room])
    print(f"{room}: {new_temp[room]}°C ==> {controller.control_heater()}")

         
      
   
       
       

