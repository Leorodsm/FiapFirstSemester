package br.com.fiap.main;

import br.com.fiap.bean.ArCondicionadoPDF4;

public class MainArCondicionado {
    public static void main(String[] args) {
        ArCondicionadoPDF4 arCondicionado = new ArCondicionadoPDF4();

        arCondicionado.temperatura = 25;
        arCondicionado.modo = "econômico";

        arCondicionado.diminuirTemperatura();
        arCondicionado.diminuirTemperatura();
        arCondicionado.trocarModo("Potente");

        System.out.println("Temperatura: "+arCondicionado.temperatura+"\nModo: "+arCondicionado.modo);
    }
}
