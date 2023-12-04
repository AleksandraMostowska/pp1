# 13.	In the TV class, add support for volume adjustment in the range 0 to 10. 
# The initial value of the volume level is 0. Add two methods to increase and decrease the 
# TV volume level by one. Note that you cannot increase or decrease the volume beyond the specified range. 
# Display the current volume level in the show_status() method. 
# Then check the operation of the TV by adjusting and displaying its volume level.

from dataclasses import dataclass

@dataclass
class TV:
    is_on: bool = False
    channel_no: int = 1
    channels = []
    volume: int = 0

    def set_channels(self, channel_list: list[str]):
        if isinstance(channel_list, list):
            self.channels = channel_list
    
    def show_channels(self):
        if self.channels:
            for i, ch in enumerate(self.channels):
                print(f'{i + 1}. {ch}', end='\n')
            print()
        else:
            print('No channels')

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
    
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, new_channel_no: int):
        if isinstance(new_channel_no, int):
            self.channel_no = new_channel_no
    
    def show_status(self):
        if self.is_on:
            if self.channel_no <= len(self.channels):
                print(f'TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}')
            else:
                print(f'TV is on, channel {self.channel_no}, volume {self.volume}')
        else:
            print('TV is off')

def main() -> None:
    tv = TV()
    tv.show_status()
    tv.show_channels()
    tv.turn_on()
    tv.set_channels(['TVN', 'Filmbox', 'Discovery'])
    tv.increase_volume()
    tv.increase_volume()
    tv.increase_volume()
    tv.show_channels()
    tv.show_status()
    tv.set_channel(2)
    tv.set_channel(5)
    tv.decrease_volume()
    tv.show_status()
    tv.turn_off()
    tv.show_status()

if __name__ == '__main__':
    main()