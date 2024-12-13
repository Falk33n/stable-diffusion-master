import { SECRET_SERVER_URL } from '$env/static/private';
import { ImageGeneratorRequestSchema } from '$server';
import { error, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const requestJson = await request.json();

	const parsedRequest = ImageGeneratorRequestSchema.safeParse(requestJson);
	if (!parsedRequest.success) {
		throw error(400, { message: 'Bad request' });
	}

	const response = await fetch(`${SECRET_SERVER_URL}/image-generator`, {
		method: 'POST',
		body: JSON.stringify(parsedRequest.data),
		headers: {
			'Content-Type': 'application/json',
		},
	});
	if (!response.ok) {
		throw error(500, { message: 'Failed to generate image' });
	}

	return new Response(await response.arrayBuffer(), {
		headers: {
			'Content-Type':
				response.headers.get('Content-Type') || 'application/octet-stream',
			'Cache-Control': 'no-store',
		},
	});
};
