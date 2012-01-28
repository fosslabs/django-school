CKEDITOR.plugins.add( 'audio',
{
	init: function( editor )
	{
        editor.addCommand( 'insertAudio', new CKEDITOR.dialogCommand( 'audioDialog' ) );
        editor.ui.addButton('Audio',
        {
            label: 'Insert Audio',
            command: 'insertAudio',
            icon: this.path + 'images/icon.png'
        });
	}
} );
CKEDITOR.dialog.add('audioDialog', function(editor) {
    return {
        title: 'Audio properties',
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
                        id: 'url',
                        label: 'Audio url',
                        validate: CKEDITOR.dialog.validate.notEmpty("Url field cannot be empty"),
                    },
                    {
                        type: 'text',
                        id: 'width',
                        label: 'Widget width',
                        validate: CKEDITOR.dialog.validate.notEmpty("Width field cannot be empty"),
                        'default': 320,
                    },
                ],
            },
        ],

        onOk: function() {
            var url = this.getValueOf('tab1', 'url');
            var width = this.getValueOf('tab1', 'width');
            var code = '<object type="application/x-shockwave-flash" data="/media/player_mp3_maxi.swf" width="' + width + '" height="20"> <param name="movie" value="/media/player_mp3_maxi.swf" /> <param name="FlashVars" value="mp3=' + url + '&width='+width+'&showvolume=1&volume=200" /> <param name=wmode value=opaque /> </object>';
            editor.insertHtml(code);
        },
    };
});
