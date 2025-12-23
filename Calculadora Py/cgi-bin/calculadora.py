from pyscript import document
print("Hello World, From the Web")
output_div = document.querySelector("textarea")
output_div.innerText = "Hello World, From the Web"