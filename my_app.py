from kivy.app import App  # Importa a classe base para criar uma aplicação Kivy
from kivy.uix.screenmanager import ScreenManager, Screen  # Importa o gerenciador de ecrãs e a classe base de ecrãs
from kivy.uix.boxlayout import BoxLayout  # Importa o layout baseado em caixas
from kivy.uix.button import Button  # Importa o widget de botão
from kivy.uix.label import Label  # Importa o widget de rótulo
from kivy.uix.textinput import TextInput  # Importa o widget de entrada de texto
from kivy.uix.scrollview import ScrollView  # Importa o widget para rolagem de conteúdo


# Define uma classe personalizada de botão para navegação entre ecrãs
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)  # Inicializa o botão padrão
        self.screen = screen  # Referência ao ecrã atual
        self.direction = direction  # Direção da transição
        self.goal = goal  # Nome do ecrã de destino

    def on_press(self):
        # Define a direção da transição e muda para o ecrã de destino
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

# Ecrã principal com botões para navegar para outros ecrãs
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Inicializa o ecrã padrão
 
        # Layout principal (vertical)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        # Layout horizontal que agrupa o texto e os botões
        hl = BoxLayout()
        txt = Label(text='Escolhe um ecrã')  # Texto de instrução

        # Adiciona botões ao layout vertical
        vl.add_widget(ScrButton(self, direction='down', goal='first', text="1"))
        vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
        vl.add_widget(ScrButton(self, direction='up', goal='third', text="3"))
        vl.add_widget(ScrButton(self, direction='right', goal='fourth', text="4"))
 
        # Adiciona o texto e os botões ao layout horizontal
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)  # Adiciona o layout horizontal ao ecrã

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout vertical centralizado
        vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Botões
        btn = Button(text='Escolha: 1', size_hint=(.5, 1), pos_hint={'left': 0})  # Botão de escolha
        btn_back = ScrButton(self, direction='up', goal='main', text="Voltar", size_hint=(.5, 1), pos_hint={'right': 1})  # Botão de retorno
        
        # Adiciona os botões ao layout
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal
        vl = BoxLayout(orientation='vertical')
        self.txtlbl = Label(text='Escolha: 2')  # Rótulo inicial
        vl.add_widget(self.txtlbl)
        
        # Layout horizontal para campo de entrada
        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl1 = Label(text='Introduza a palavra-passe:', halign='right')  # Rótulo
        self.txtinput = TextInput(multiline=False)  # Campo de entrada
        
        hl_0.add_widget(lbl1)
        vl.add_widget(hl_0)
        hl_0.add_widget(self.txtinput)
        
        # Layout para botões
        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        btn_false = Button(text="OK!")
        btn_back = ScrButton(self, direction='right', goal='main', text="Voltar")
        
        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        vl.add_widget(hl)
        self.add_widget(vl)
        
        # Evento do botão OK
        btn_false.on_press = self.change_text
    
    def change_text(self):
        self.txtlbl.text = self.txtinput.text + '? Isto não funcionou ...'

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout vertical
        layout = BoxLayout(orientation='vertical')
        btn_back = ScrButton(self, direction='down', goal='main', text="Voltar", size_hint=(1, None), height='40sp')
        test_label = Label(text="O seu ecrã personalizado")
        
        layout.add_widget(test_label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        vl = BoxLayout(orientation='vertical', spacing=8)  # Layout vertical
        a = 'INICIAR ' + 'Escolha: 3 ' * 200  # Texto longo para demonstração de scroll
 
        test_label = Label(text="Tarefa Adicional", size_hint=(0.3, None))  # Rótulo superior
        btn_back = ScrButton(self, direction='left', goal='main', text="Voltar", size_hint=(1, .2), pos_hint={'center-x': 0.5})  # Botão de retorno
        
        # Rótulo de texto longo com rolagem
        self.label = Label(text= a, size_hint_y=None, font_size='24sp', halign='left', valign='top')  
        self.label.bind(size=self.resize)  # Redimensiona automaticamente o texto
        
        self.scroll = ScrollView(size_hint=(1, 1))  # Widget de rolagem
        self.scroll.add_widget(self.label)  # Adiciona o rótulo ao scrollview

        vl.add_widget(test_label)  # Adiciona o rótulo ao layout
        vl.add_widget(btn_back)  # Adiciona o botão de retorno ao layout
        vl.add_widget(self.scroll)  # Adiciona o scrollview ao layout
        self.add_widget(vl)  # Adiciona o layout ao ecrã
 
    def resize(self, *args):
        # Ajusta o tamanho do texto com base no tamanho do rótulo
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]
                
# Aplicação principal
class MyApp(App):
    def build(self):
        sm = ScreenManager()  # Gerenciador de ecrãs
        sm.add_widget(MainScr(name='main'))  # Adiciona o ecrã principal
        sm.add_widget(FirstScr(name='first'))  # Adiciona o primeiro ecrã
        sm.add_widget(SecondScr(name='second'))  # Adiciona o segundo ecrã
        sm.add_widget(ThirdScr(name='third'))  # Adiciona o terceiro ecrã
        sm.add_widget(FourthScr(name='fourth'))  # Adiciona o quarto ecrã
        return sm  # Retorna o gerenciador de ecrãs
 
MyApp().run()  # Executa a aplicação
