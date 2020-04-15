function autoCalcSetup() {
  $("form[name=cart]").jAutoCalc("destroy");
  $("form[name=cart] tr[name=line_items]").jAutoCalc({
    keyEventsFire: true,
    decimalPlaces: 2,
    emptyAsZero: true
  });
  $("form[name=cart]").jAutoCalc({ decimalPlaces: 2 });
}
autoCalcSetup();
$("button[name=remove]").click(function(e) {
  e.preventDefault();
  var form = $(this).parents("form");
  $(this)
    .parents("tr")
    .remove();
  autoCalcSetup();
});

var x = 0;

$(".dish").click(function(e) {
    var id_str = this.id.toString();
    console.log(id_str);
  e.preventDefault();

  var $table = $("table");
  var $top = $table.find("tr[name=line_items]").first();
  var $new = $top.clone(true);
  console.log($new);
  $new.jAutoCalc("destroy");
  $new.insertBefore($top);
  $new.find("input[type=text]").val("");
  $new.find("input[name=price]").val(document.getElementById('price_' + id_str).innerHTML);
  $new.find("input[name=item]").val((document.getElementById(id_str).innerHTML).trim());
  $new.find("input[name=qty]").val("1");
  $new.find("input[name=qty]").attr("id", );
  autoCalcSetup();
  x++;
  console.log(x);
});

function init(){
    const categories = document.querySelectorAll(".category");
    const nav_items = document.querySelectorAll(".nav-item");

    categories.forEach((category, index) => {
       category.addEventListener('click', function(){
            changeCategory(this);
       });
    });

    function changeCategory(category){
        categories.forEach(category => {
            category.classList.remove("active");
        });
        category.classList.add("active");
    }
}

init();