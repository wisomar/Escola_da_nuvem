import os
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

# Obter o diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para salvar o arquivo de áudio
output_path = 
os.path.join(current_dir, "speech.wav")

# Carregar os modelos
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Solicitar ao usuário que digite a mensagem
mensagem = input("Digite a mensagem que deseja converter em fala: ")

# Processar a entrada do texto
inputs = processor(text=mensagem, return_tensors="pt")

# Carregar xvector contendo as características da voz do falante de um dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

# Gerar a fala
speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

# Salvar o áudio gerado em um arquivo
sf.write(output_path, speech.numpy(), samplerate=16000)

print(f"Áudio salvo como: {output_path}")
