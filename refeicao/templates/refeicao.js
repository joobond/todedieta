let alimentosjs = []

$(function() {
    $("#descAlimento").autocomplete({
      source: "/busca-alimento",
      minLength: 3,
    });
  });