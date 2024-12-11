<script lang="ts">
	import type { TypographyProps } from '$components/typography';
	import { cn } from '$utils';

	let { children, class: className, ...props }: TypographyProps = $props();
</script>

<p
	class={cn('leading-7 [&:not(:first-child)]:mt-6', className)}
	{...props}
>
	{@render children?.()}
</p>
