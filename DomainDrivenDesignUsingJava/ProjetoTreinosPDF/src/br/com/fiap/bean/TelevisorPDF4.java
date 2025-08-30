package br.com.fiap.bean;

public class TelevisorPDF4 {
    public int volume;
    public int canal;

    public void aumentarVolume() {
        volume ++;
    }

    public void diminuirVolume() {
        volume --;
    }

    public void trocarCanal(int novoCanal) {
        canal = novoCanal;
    }
}
