tinymce.init({
    selector: "textarea",
    theme: "modern",
    plugins: [
        "autolink lists link hr anchor",
        "searchreplace wordcount visualblocks visualchars fullscreen",
        "insertdatetime nonbreaking save table contextmenu directionality",
        "paste  "
    ],
    toolbar1: " undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent",
});
