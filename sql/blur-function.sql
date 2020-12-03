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
	# so we have to do sigma=(sigma, sigma, 0)
    blurred = ndimage.gaussian_filter(img_array, sigma=(5, 5, 0))

    # return in bytes format
    return blurred.tobytes()

$BODY$;

ALTER FUNCTION public.bytea_blur(bytea)
    OWNER TO postgres;
