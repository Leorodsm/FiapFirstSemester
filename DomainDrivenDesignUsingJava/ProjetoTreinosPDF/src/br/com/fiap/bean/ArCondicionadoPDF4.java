package br.com.fiap.bean;

public class ArCondicionadoPDF4 {
    public int temperatura;
    public String modo;

    // Métodos da Classe

    public void aumentarTemperatura() {
        temperatura ++;
    }

    public void diminuirTemperatura() {
        temperatura --;
    }

    public void trocarModo(String novoModo) {
        modo = novoModo;
    }
}