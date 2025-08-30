package br.com.fiap.bean;

import java.time.LocalDate;

public class Pessoa {

    // Atributos

    private String nome;
    private int anoNascimento;

    // Construtores

    public Pessoa() {
    }

    public Pessoa(String nome, int anoNascimento) {
        this.nome = nome;
        this.anoNascimento = anoNascimento;
    }

    // Métodos getters/setters

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAnoNascimento() {
        return anoNascimento;
    }

    public void setAnoNascimento(int anoNascimento) {
        LocalDate dataAtual = LocalDate.now();

        try {
            if(anoNascimento >= 1900 && anoNascimento <= dataAtual.getYear()) {
                this.anoNascimento = anoNascimento;
            } else {
                throw new Exception("Valor inválido! (min = 1900 até max = Ano atual");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }


    // Métodos da Classe

    public int calcularIdade(int anoAtual) {
        return anoAtual - anoNascimento;
    }
}
