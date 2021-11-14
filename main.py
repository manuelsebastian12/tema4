"""Programa principal"""
import clases

a = input("Ingrese el nombre de la persona ")

gerente1 = clases.Gerente(a)
gerente1.NombreEmpresa()
gerente1.entrevistar()
gerente1.trabajar()
gerente1.vestir()
gerente1.getEstatura()