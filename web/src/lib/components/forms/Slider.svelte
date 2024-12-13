<script lang="ts">
	import { cn } from '$utils';
	import {
		Slider,
		type SliderRootProps,
		type WithoutChildrenOrChild,
	} from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		value = $bindable([0]),
		...props
	}: WithoutChildrenOrChild<SliderRootProps> = $props();
</script>

<Slider.Root
	bind:ref
	bind:value
	class={cn(
		'relative flex w-full touch-none select-none items-center',
		className,
	)}
	{...props}
>
	{#snippet children({ thumbs })}
		<span
			class="bg-primary/20 relative h-1.5 w-full grow overflow-hidden rounded-full"
		>
			<Slider.Range class="bg-primary absolute h-full" />
		</span>
		{#each thumbs as thumb}
			<Slider.Thumb
				index={thumb}
				class="border-primary/50 bg-background focus-visible:ring-ring block size-4 rounded-full border shadow transition-colors focus-visible:outline-none focus-visible:ring-1 disabled:pointer-events-none disabled:opacity-50"
			/>
		{/each}
	{/snippet}
</Slider.Root>
