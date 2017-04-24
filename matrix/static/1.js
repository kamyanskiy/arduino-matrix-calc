$(document).ready(function() {
  $(".seatselect").click(function(){
    $(this).toggleClass('label-success');
    checkbox = $(this.children)[0]
    if (checkbox.hasAttribute("checked")) {
        checkbox.removeAttribute('checked');
        checkbox.value = '0'
    } else {
        checkbox.setAttribute('checked', 'checked');
        checkbox.value = '1';
    }
});
});