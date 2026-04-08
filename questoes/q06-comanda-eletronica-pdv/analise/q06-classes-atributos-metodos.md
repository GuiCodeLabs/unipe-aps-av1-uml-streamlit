# 🧾 Questão 06 — Classes, Atributos e Métodos

## 🟦 Classe Produto

### Atributos
- codigo : int  
- nome : string  
- valorUnitario : decimal  

### Métodos
- cadastrar()  
- editarPreco()  

---

## 🟨 Classe ItemComanda

### Atributos
- quantidade : int  
- /produto : Produto  

### Métodos
- calcularSubtotal()  

---

## 🟩 Classe Comanda

### Atributos
- numero : int  
- status : string  
- /itens : List<ItemComanda>  

### Métodos
- adicionarItem(produto, quantidade)  
- removerItem(item)  
- calcularTotal()  
- finalizarCompra()  

---

## 🟥 Classe Caixa

### Atributos
- comandas : List<Comanda>  

### Métodos
- abrirComanda(numero)  
- buscarComanda(numero)  
- registrarConsumo(numeroComanda, produto, quantidade)  
- fecharComanda(numeroComanda)  