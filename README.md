# Remove BG - Ferramenta Automática de Remoção de Fundo 🎨🚀
Este é um script em Python que remove automaticamente o fundo de imagens com alta precisão usando inteligência artificial. 
Ideal para designers, editores e criadores de conteúdo!

## 📌 Sobre o Projeto
Este projeto utiliza a biblioteca `rembg` para remover automaticamente o fundo de imagens. Ele processa arquivos no formato PNG e salva uma versão sem fundo, ideal para designers, criadores de conteúdo e automação de edição de imagens.

## 🚀 Tecnologias Utilizadas
- Python 3+
- `rembg` para remoção de fundo
- `Pillow` para manipulação de imagens
- `onnxruntime` para otimização do processamento

## 📜 Como Usar
### 1️⃣ Instale as dependências
```sh
pip install rembg pillow onnxruntime
```

### 2️⃣ Execute o script
```sh
python main.py
```

### 3️⃣ Verifique a saída
A imagem processada será salva no mesmo diretório com o nome `sgame_no_bg.png`.

## ⚠️ Possíveis Erros e Soluções
- **ModuleNotFoundError: No module named 'rembg'**
  - Instale o pacote com `pip install rembg`
- **[Errno 2] No such file or directory: 'sgame.png'**
  - Verifique se a imagem está na mesma pasta do script ou forneça o caminho completo

## 📌 Contribuições
Sinta-se à vontade para contribuir com melhorias, sugestões e otimizações para este projeto!

## 📜 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

---
🛠 Desenvolvido para automação e eficiência na remoção de fundos de imagens. 🚀

rembg, remove-background, ai, machine-learning, image-processing, python

