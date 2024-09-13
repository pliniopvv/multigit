from tkinter import *
from tkinter import filedialog
from Kernel import ImplKernel as Kernel
from Models import Repository























class MainWindow:
    def _reupdate(self, size = None):
        self.win.destroy()
        self._update(size)

    def __init__(self, size = None):
        self._update(size)

    def _update(self, size = None):
        app = Tk()
        app.title("Repositórios configurados")
        if (size != None):
            app.geometry(size)
        self.win = app
        
        self._build()
        
        app.protocol("WM_DELETE_WINDOW", lambda : self._close())
        self.win.mainloop()

    def _build(self):
        # override with build components in 'self.win'
        pass

    def _close(self):
        self.win.destroy()
    
    pass



class ListRepository(MainWindow):
    def __init__(self):
        super().__init__("200x400")

    def _build(self):
        app = self.win
        label = Label(app, text="Repositórios:")
        label.pack()

        listbox = Listbox(app)

        repos = Kernel.config.getRepositorios()
        for repo in repos:
            listbox.insert(repos.index(repo), repo.name)

        listbox.pack(padx=0, expand=True, fill=['both'])
        self.listbox = listbox

        button_add = Button(app, text="Adicionar", command=self.add_repository)
        button_add.pack(fill=['x'])

        button_del = Button(app, text="Excluir", command=self.del_repository)
        button_del.pack(fill=['x'])

        pass

    def add_repository(self):
        def save_repo(repo):
            Kernel.config.addRepositorio(repo)
        self.modal = AddRepository(lambda repo: save_repo(repo))

    def del_repository(self):
        selection = self.listbox.curselection()
        lista = Kernel.config.getRepositorios()
        repo = lista[selection[0]]
        Kernel.config.removeRepositorio(repo)
        self._reupdate("200x400")
        pass




class AddRepository(MainWindow):
    def __init__(self, onClose):
        if (onClose == None): raise ValueError("Função OnClose não definida.")

        self.input = {}
        self.view = {}
        self.onClose = onClose
        super().__init__()

    def _build(self):
        app = self.win

        labelNome = Label(app, text="Nome do repositório:")
        labelNome.pack(pady=5, padx=5)

        nome = Entry(app, width=65)
        nome.pack(pady=5, padx=5)

        labelRootRepo = Label(app, text="Root do repositório:")
        labelRootRepo.pack(pady=5, padx=5)

        entry_root = StringVar()
        self.input['chooser'] = entry_root
        RootRepo = Entry(app, width=65, state='disabled', textvariable=entry_root)
        RootRepo.pack(pady=5, padx=5)

        buttonSave = Button(app, text="Ok", command=self.save)
        buttonSave.pack(fill=['x'])

        buttonFChooser = Button(app, text="Selecionar", command=lambda : self.fchooser(lambda directory: entry_root.set(directory)))
        buttonFChooser.pack(fill=['x'])

        self.input['nome'] = nome
        self.input['path'] = entry_root

    def fchooser(self, onFinish):
        directory = filedialog.askdirectory()
        onFinish(directory)
        self.win.update()

    def save(self):
        nome = self.input['nome'].get()
        path = self.input['path'].get()
        repo = Repository(nome, path)
        self.onClose(repo)
        pass