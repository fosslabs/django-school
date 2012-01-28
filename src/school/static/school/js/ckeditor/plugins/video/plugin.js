CKEDITOR.plugins.add( 'video',
{
	init: function( editor )
	{
        editor.addCommand( 'insertVideo', new CKEDITOR.dialogCommand( 'videoDialog' ) );
        editor.ui.addButton('Video',
        {
            label: 'Insert Video',
            command: 'insertVideo',
            icon: this.path + 'images/icon.gif'
        });
	}
} );
CKEDITOR.dialog.add('videoDialog', function(editor) {
    return {
        title: 'Video properties',
        minWidth: 240,
        minHeight: 100,
        
        contents:
        [
            {
                id: 'tab1',
                label: 'Basic settings',
                elements:
                [
                    {
                        type: 'text',
                        id: 'youtubeid',
                        label: 'Youtube id',
                        validate: CKEDITOR.dialog.validate.notEmpty("Youtube id field cannot be empty"),
                    },
                    {
                        type: 'text',
                        id: 'width',
                        label: 'Width',
                        validate: CKEDITOR.dialog.validate.notEmpty("Width field cannot be empty"),
                        'default': 500,
                    },
                    {
                        type: 'text',
                        id: 'height',
                        label: 'Height',
                        validate: CKEDITOR.dialog.validate.notEmpty("Height field cannot be empty"),
                        'default': 350,
                    },
                ],
            },
        ],

        onOk: function() {
            var id = this.getValueOf('tab1', 'youtubeid');
            var width = this.getValueOf('tab1', 'width');
            var height = this.getValueOf('tab1', 'height');
            var code = '<iframe width="'+width+'" height="'+height+'" src="http://www.youtube.com/embed/'+id+'" frameborder="0" allowfullscreen></iframe>'
            editor.insertHtml(code);
        },
    };
});
