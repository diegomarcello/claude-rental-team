// Adds a copy button to code blocks. The site works without it.
if (navigator.clipboard) {
  for (const block of document.querySelectorAll("pre")) {
    const wrapper = document.createElement("div");
    wrapper.className = "code";
    block.replaceWith(wrapper);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy";
    button.textContent = "Copiar";
    button.setAttribute("aria-live", "polite");
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(block.textContent);
        button.textContent = "Copiado";
      } catch {
        button.textContent = "Falhou";
      }
      setTimeout(() => { button.textContent = "Copiar"; }, 2000);
    });

    wrapper.append(block, button);
  }
}
