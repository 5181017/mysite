 function showToast(str) {
     toastr.options = {
         "positionClass": "toast-bottom-center",
         "timeOut": "1000",
     };

     toastr.success(str);
 }


 function showToastError(str) {
     toastr.options = {
         "positionClass": "toast-bottom-center",
         "timeOut": "1000",
     };

     toastr.error(str);
 }