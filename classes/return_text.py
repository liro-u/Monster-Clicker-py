import pygame


class Text:
    """
    cette classe s'occupe du parametrage des textes,
    il faut y entrer:
          txt,
          x,
          y,
          width,          (taille maxi de la fenetre)
          taille,          (de la police)
          police,
          col,
          txt_align          (left/right/center/justify)

    pour afficher le texte il faut entrer :
          show(
            surface
            )
    """

    def __init__(self, txt, x, y, width, taille, police, col, bg, txt_align):
        self.txt = txt
        self.x = x
        self.y = y
        self.width = width
        self.taille = taille
        self.col = col
        self.bg = bg
        self.txt_align = txt_align

        self.font = pygame.font.Font(police, taille)
        temp = self.render(' ')
        self.space = temp.get_width()
        self.height = temp.get_height()
        self.surface = pygame.Surface((self.width, 600))

        self.rendered = []
        self.words = []
        for word in self.txt.split(' '):
            if '\n' in word:
                separe = word.split('\n')
                self.words.append(separe[0])
                self.rendered.append(self.render(separe[0]))
                self.words.append('§' + separe[1])
                self.rendered.append(self.render(separe[1]))
            else:
                self.words.append(word)
                self.rendered.append(self.render(word))

        self.update()

    def render(self, text):
        return self.font.render(text, 1, self.col)

    def update(self):

        self.surface.fill(self.bg)

        self.lines = ['']
        self.lines_txt = [[]]
        current = 0
        for index, word in enumerate(self.rendered):
            current += word.get_width() + self.space
            if current - self.space <= self.width and not '§' in self.words[index]:
                self.lines[-1] += self.words[index] + ' '
                self.lines_txt[-1].append(self.words[index])
            else:
                if '§' in self.words[index]:   self.words[index] = self.words[index][1:]
                self.lines[-1] = self.lines[-1][:-1]
                self.lines.append(self.words[index] + ' ')
                self.lines_txt[-1].append(current - word.get_width() - self.space)
                self.lines_txt.append([self.words[index]])
                current = word.get_width() + self.space
        self.lines_txt[-1].append(current)

        if self.txt_align == 'left':
            for index, line in enumerate(self.lines):
                self.surface.blit(self.render(line), (0, self.height * index))

        elif self.txt_align == 'center':
            for index, line in enumerate(self.lines):
                render = self.render(line)
                self.surface.blit(render, (self.width - render.get_width() // 2, self.height * index))

        elif self.txt_align == 'right':
            for index, line in enumerate(self.lines):
                render = self.render(line)
                self.surface.blit(render, (self.width - render.get_width(), self.height * index))

        elif self.txt_align == 'justify':
            count = 0
            for yoff, line in enumerate(self.lines_txt):
                length = 0
                total = int(line[-1]) - self.space * (len(line) - 1)
                if len(line) > 2:
                    space = (self.width - total) / (len(line) - 2)
                else:
                    space = 0
                for index, word in enumerate(line[:-1]):
                    self.surface.blit(self.rendered[count], (length, self.height * yoff))
                    length += self.rendered[count].get_width() + space
                    count += 1

    def show(self, surface):
        surface.blit(self.surface, (self.x, self.y))
