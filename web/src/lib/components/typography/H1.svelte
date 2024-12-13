<script
	module
	lang="ts"
>
	export type TypographyProps = HTMLAttributes<
		HTMLHeadingElement | HTMLParagraphElement
	>;
</script>

<script lang="ts">
	import { cn } from '$utils';
	import type { HTMLAttributes } from 'svelte/elements';

	let { children, class: className, ...props }: TypographyProps = $props();
</script>

<h1
	class={cn(
		'scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl',
		className,
	)}
	{...props}
>
	{@render children?.()}
</h1>
