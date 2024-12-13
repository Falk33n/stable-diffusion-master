import { z } from 'zod';

export const ImageGeneratorRequestSchema = z.object({
	prompt: z.string(),
	negative_prompt: z.string().or(z.null()).nullable(),
	inference_steps: z.number().int().min(2).max(100),
	guidance_scale: z.number(),
});
