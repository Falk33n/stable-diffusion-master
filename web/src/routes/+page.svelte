<script lang="ts">
	import {
		PUBLIC_DEFAULT_GUIDANCE_SCALE,
		PUBLIC_DEFAULT_INFERENCE_STEPS,
		PUBLIC_MAX_GUIDANCE_SCALE,
		PUBLIC_MAX_INFERENCE_STEPS,
		PUBLIC_MIN_GUIDANCE_SCALE,
		PUBLIC_MIN_INFERENCE_STEPS,
	} from '$env/static/public';

	type FormData = {
		prompt?: string;
		negative_prompt: string | null;

		/** Must be between 2 and 100 */
		inference_steps: number;

		/** Must be between 0 and 10 */
		guidance_scale: number;
	};

	function resetFormData(): FormData {
		return {
			prompt: undefined,
			negative_prompt: null,
			inference_steps: Number(PUBLIC_DEFAULT_INFERENCE_STEPS),
			guidance_scale: Number(PUBLIC_DEFAULT_GUIDANCE_SCALE),
		};
	}

	let formData = $state<FormData>(resetFormData());

	function validateNumberRange(min: number, max: number, value: number) {
		if (value < min || value > max) return false;

		return true;
	}

	async function generateImage() {
		const data = formData;

		formData = resetFormData();

		if (
			!validateNumberRange(
				Number(PUBLIC_MIN_INFERENCE_STEPS),
				Number(PUBLIC_MAX_INFERENCE_STEPS),
				data.inference_steps,
			) ||
			!validateNumberRange(
				Number(PUBLIC_MIN_GUIDANCE_SCALE),
				Number(PUBLIC_MAX_GUIDANCE_SCALE),
				data.guidance_scale,
			)
		) {
			return;
		}

		const response = await fetch('/api/image-generator', {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				'Content-Type': 'application/json',
			},
		});

		if (!response.ok) return;

		const blob = await response.blob();

		const url = URL.createObjectURL(blob);

		const img = document.createElement('img');
		img.src = url;

		if (data.prompt) {
			img.alt = data.prompt;
		}

		const outputDiv = document.getElementById('output');
		if (outputDiv) {
			outputDiv.appendChild(img);
		}

		img.onload = () => {
			URL.revokeObjectURL(url);
		};
	}
</script>

<form
	onsubmit={async (e) => {
		e.preventDefault();
		await generateImage();
	}}
>
	<input
		type="text"
		name="prompt"
		bind:value={formData.prompt}
	/>
	<button
		type="submit"
		disabled={!formData.prompt}>Submit</button
	>
</form>

<div id="output"></div>
