package br.com.fiap.bean;

public class RadioPDF4 {

    // Atributos
    public int volume;
    public float estacao;

    // Métodos
    public void aumentarVolume() {
        volume ++;
    }

    public void diminuirVolume() {
        volume --;
    }

    public void trocarEstacao(float frequencia) {
        estacao = frequencia;
    }
}
