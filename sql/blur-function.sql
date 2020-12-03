-- FUNCTION: public.bytea_blur(bytea)

-- DROP FUNCTION public.bytea_blur(bytea);

CREATE OR REPLACE FUNCTION public.bytea_blur(
	data bytea)
    RETURNS bytea
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE

AS $BODY$
    from PIL import Image
    from scipy import ndimage
    import io
    import numpy as np

    img_array = np.array(Image.open(io.BytesIO(data)))

    # sigma=sigma applies the filter to each dimension,
    # including the third axis that holds the color channel
    # so we have to pass in sigma=(sigma, sigma, 0) instead
    blurred = ndimage.gaussian_filter(img_array, sigma=(5, 5, 0))

    # Turn array back to Image
    blurred_img = Image.fromarray(blurred)

    # Create new in-memory file-like object
    return_buffer = io.BytesIO()

    # Save the image in the file-like object
    blurred_img.save(return_buffer, "JPEG")

    # Get bytes from object
    return return_buffer.getvalue()

$BODY$;

ALTER FUNCTION public.bytea_blur(bytea)
    OWNER TO postgres;