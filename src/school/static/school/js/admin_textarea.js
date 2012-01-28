django.jQuery(function() {
    CKEDITOR.replace('id_html',
    {
        filebrowserBrowseUrl : '/admin/filebrowser/browse/?pop=3',
        extraPlugins : 'audio,video',
    });
});
